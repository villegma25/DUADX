-- ============================================
-- EJERCICIO 2: TRANSACCIÓN DE COMPRA
-- ============================================

DO $$
DECLARE
    v_user_id INTEGER := 1;
    v_bill_id INTEGER;

    v_product_id INTEGER;
    v_quantity INTEGER;
    v_stock INTEGER;
    v_price NUMERIC(10, 2);
    v_total NUMERIC(10, 2) := 0;

    -- Productos que se desean comprar
    v_products INTEGER[] := ARRAY[1, 2, 3];
    v_quantities INTEGER[] := ARRAY[1, 2, 1];

    i INTEGER;
BEGIN

    -- ========================================
    -- 1. VALIDAR QUE EL USUARIO EXISTE
    -- ========================================

    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe', v_user_id;
    END IF;


    -- ========================================
    -- 2. VALIDAR PRODUCTOS Y EXISTENCIAS
    -- ========================================

    IF array_length(v_products, 1) <> array_length(v_quantities, 1) THEN
        RAISE EXCEPTION
            'La cantidad de productos no coincide con la cantidad de cantidades';
    END IF;


    FOR i IN 1..array_length(v_products, 1)
    LOOP

        v_product_id := v_products[i];
        v_quantity := v_quantities[i];

        -- Buscar producto
        SELECT stock, price
        INTO v_stock, v_price
        FROM products
        WHERE id = v_product_id
        FOR UPDATE;

        -- Verificar que existe
        IF NOT FOUND THEN
            RAISE EXCEPTION
                'El producto con ID % no existe',
                v_product_id;
        END IF;

        -- Validar cantidad
        IF v_quantity <= 0 THEN
            RAISE EXCEPTION
                'La cantidad del producto % debe ser mayor que cero',
                v_product_id;
        END IF;

        -- Validar stock
        IF v_stock < v_quantity THEN
            RAISE EXCEPTION
                'Stock insuficiente para el producto %. Stock disponible: %, solicitado: %',
                v_product_id,
                v_stock,
                v_quantity;
        END IF;

        -- Calcular total
        v_total := v_total + (v_price * v_quantity);

    END LOOP;


    -- ========================================
    -- 3. CREAR LA FACTURA
    -- ========================================

    INSERT INTO bills (
        user_id,
        total,
        status
    )
    VALUES (
        v_user_id,
        v_total,
        'Completada'
    )
    RETURNING id INTO v_bill_id;


    -- ========================================
    -- 4. INSERTAR PRODUCTOS DE LA FACTURA
    -- ========================================

    FOR i IN 1..array_length(v_products, 1)
    LOOP

        v_product_id := v_products[i];
        v_quantity := v_quantities[i];

        SELECT price
        INTO v_price
        FROM products
        WHERE id = v_product_id;

        INSERT INTO bill_products (
            bill_id,
            product_id,
            quantity,
            unit_price
        )
        VALUES (
            v_bill_id,
            v_product_id,
            v_quantity,
            v_price
        );

    END LOOP;


    -- ========================================
    -- 5. REDUCIR EL STOCK
    -- ========================================

    FOR i IN 1..array_length(v_products, 1)
    LOOP

        v_product_id := v_products[i];
        v_quantity := v_quantities[i];

        UPDATE products
        SET stock = stock - v_quantity
        WHERE id = v_product_id;

    END LOOP;


    -- ========================================
    -- FINAL
    -- ========================================

    RAISE NOTICE
        'Compra realizada correctamente. Factura ID: %, Total: %',
        v_bill_id,
        v_total;

END $$;