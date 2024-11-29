const express = require('express');
const router = express.Router();
const Cart = require('../models/cart');
const CartItem = require('../models/cartItem');

router.post('/', async (req, res) => {
    const { userId } = req.body;

    try {
        const cart = new Cart({ userId });
        await cart.save();
        res.status(201).json(cart);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

router.post('/:cartId/items', async (req, res) => {
    const { cartId } = req.params;
    const { productId, quantity } = req.body;

    try {
        const cartItem = new CartItem({ cartId, productId, quantity });
        await cartItem.save();
        res.status(201).json(cartItem);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

router.get('/:cartId/items', async (req, res) => {
    const { cartId } = req.params;

    try {
        const cartItems = await CartItem.find({ cartId }).populate('productId');
        res.json(cartItems);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

module.exports = router;
