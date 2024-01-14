import { describe,test,expect } from "vitest";

describe('Import Vue components', () => {
    test('AddToCartBtn import', async () => {
        const cmp = await import('../components/AddToCartBtn.vue');
        expect(cmp).toBeDefined();
    });

    test('AddToCartViewer import', async () => {
        const cmp = await import('../components/AddToCartViewer.vue');
        expect(cmp).toBeDefined();
    });

    test('AlertItemTemporary import', async () => {
        const cmp = await import('../components/AlertItemTemporary.vue');
        expect(cmp).toBeDefined();
    });

    test('AlertsGroup import', async () => {
        const cmp = await import('../components/AlertsGroup.vue');
        expect(cmp).toBeDefined();
    });

    test('CartCheckout import', async () => {
        const cmp = await import('../components/CartCheckout.vue');
        expect(cmp).toBeDefined();
    });

    test('CartComplete import', async () => {
        const cmp = await import('../components/CartComplete.vue');
        expect(cmp).toBeDefined();
    });

    test('CartPayment import', async () => {
        const cmp = await import('../components/CartPayment.vue');
        expect(cmp).toBeDefined();
    });

    test('CartSubtotal import', async () => {
        const cmp = await import('../components/CartSubtotal.vue');
        expect(cmp).toBeDefined();
    });

    test('CartSummary import', async () => {
        const cmp = await import('../components/CartSummary.vue');
        expect(cmp).toBeDefined();
    });

    test('CartTable import', async () => {
        const cmp = await import('../components/CartTable.vue');
        expect(cmp).toBeDefined();
    });

    test('CartTableItem import', async () => {
        const cmp = await import('../components/CartTableItem.vue');
        expect(cmp).toBeDefined();
    });

    test('CartTimeline import', async () => {
        const cmp = await import('../components/CartTimeline.vue');
        expect(cmp).toBeDefined();
    });

    test('FeaturedProductCard import', async () => {
        const cmp = await import('../components/FeaturedProductCard.vue');
        expect(cmp).toBeDefined();
    });

    test('LogoAnimation import', async () => {
        const cmp = await import('../components/LogoAnimation.vue');
        expect(cmp).toBeDefined();
    });

    test('LogoAnimationLoading import', async () => {
        const cmp = await import('../components/LogoAnimationLoading.vue');
        expect(cmp).toBeDefined();
    });

    test('ProductCard import', async () => {
        const cmp = await import('../components/ProductCard.vue');
        expect(cmp).toBeDefined();
    });

    test('TopNavCart import', async () => {
        const cmp = await import('../components/TopNavCart.vue');
        expect(cmp).toBeDefined();
    });

    test('TopNav import', async () => {
        const cmp = await import('../components/TopNav.vue');
        expect(cmp).toBeDefined();
    });
});