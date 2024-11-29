const express = require('express');
const router = express.Router();
const Order = require('../models/order');
const OrderItem = require('../models/orderItem');

router.post('/', async (req, res) => {
    const { userId, total } = req.body;

    try {
        const order = new Order({ userId, total });
        await order.save();
        res.status(201).json(order);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

router.post('/:orderId/items', async (req, res) => {
    const { orderId } = req.params;
    const { productId, quantity, price } = req.body;

    try {
        const orderItem = new OrderItem({ orderId, productId, quantity, price });
        await orderItem.save();
        res.status(201).json(orderItem);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

router.get('/:orderId/items', async (req, res) => {
    const { orderId } = req.params;

    try {
        const orderItems = await OrderItem.find({ orderId }).populate('productId');
        res.json(orderItems);
    } catch (error) {
        res.status(500).json({ message: 'Server error' });
    }
});

module.exports = router;
