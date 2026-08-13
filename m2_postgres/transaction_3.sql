-- ============================================
-- EJERCICIO 3: TRANSACCIÓN DE DEVOLUCIÓN
-- ============================================

DO $$
DECLARE
    v_bill_id INTEGER := 1;

    v_product_id INTEGER;
    v_quantity INTEGER;

    v_status VARCHAR(20);

BEGIN

    -- ========================================
    -- 1. VERIFICAR QUE LA FACTURA EXISTE
    -- ========================================

    SELECT status
    INTO v_status
    FROM bills
    WHERE id = v_bill_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION
            'La factura con ID % no existe',
            v_bill_id;
    END IF;


    -- ========================================
    -- 2. VERIFICAR QUE NO HAYA SIDO RETORNADA
    -- ========================================

    IF v_status = 'Retornada' THEN
        RAISE EXCEPTION
            'La factura % ya fue retornada',
            v_bill_id;
    END IF;


    -- ========================================
    -- 3. DEVOLVER LOS PRODUCTOS AL STOCK
    -- ========================================

    FOR v_product_id, v_quantity IN
        SELECT product_id, quantity
        FROM bill_products
        WHERE bill_id = v_bill_id
    LOOP

        UPDATE products
        SET stock = stock + v_quantity
        WHERE id = v_product_id;

    END LOOP;


    -- ========================================
    -- 4. MARCAR LA FACTURA COMO RETORNADA
    -- ========================================

    UPDATE bills
    SET status = 'Retornada'
    WHERE id = v_bill_id;


    -- ========================================
    -- FINAL
    -- ========================================

    RAISE NOTICE
        'La factura % fue retornada correctamente',
        v_bill_id;

END $$;