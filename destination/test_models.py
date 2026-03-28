"""
Model tests for the destination app.
"""

import pytest
from django.test import TestCase
from destination.models import Destination, NewsPosts, Testimonial, HomeSlider


class DestinationModelTests(TestCase):
    """Tests for the Destination model."""

    def setUp(self):
        """Set up test fixtures."""
        self.destination = Destination.objects.create(
            name='Paris',
            price=500,
            description='City of lights',
            offer=True
        )

    def test_destination_creation(self):
        """Test that a destination is created correctly."""
        self.assertEqual(self.destination.name, 'Paris')
        self.assertEqual(self.destination.price, 500)
        self.assertTrue(self.destination.offer)

    def test_destination_str(self):
        """Test the string representation of a destination."""
        expected_str = 'Paris ($500)'
        self.assertEqual(str(self.destination), expected_str)

    def test_destination_timestamps(self):
        """Test that timestamps are set correctly."""
        self.assertIsNotNone(self.destination.created_at)
        self.assertIsNotNone(self.destination.updated_at)

    def test_destination_unique_name(self):
        """Test that destination names are unique."""
        with self.assertRaises(Exception):
            Destination.objects.create(
                name='Paris',
                price=600,
                description='Another Paris'
            )


class NewsPostsModelTests(TestCase):
    """Tests for the NewsPosts model."""

    def setUp(self):
        """Set up test fixtures."""
        self.news = NewsPosts.objects.create(
            title='Travel Tips',
            date=15,
            month='March',
            category='Tips',
            content='Top 10 travel tips'
        )

    def test_news_creation(self):
        """Test that a news post is created correctly."""
        self.assertEqual(self.news.title, 'Travel Tips')
        self.assertEqual(self.news.category, 'Tips')

    def test_news_str(self):
        """Test the string representation of a news post."""
        expected_str = 'Travel Tips (March 15)'
        self.assertEqual(str(self.news), expected_str)


class TestimonialModelTests(TestCase):
    """Tests for the Testimonial model."""

    def setUp(self):
        """Set up test fixtures."""
        self.testimonial = Testimonial.objects.create(
            author='John Doe',
            position='CEO',
            content='Great service!'
        )

    def test_testimonial_creation(self):
        """Test that a testimonial is created correctly."""
        self.assertEqual(self.testimonial.author, 'John Doe')
        self.assertEqual(self.testimonial.position, 'CEO')

    def test_testimonial_str(self):
        """Test the string representation of a testimonial."""
        expected_str = 'John Doe - CEO'
        self.assertEqual(str(self.testimonial), expected_str)


class HomeSliderModelTests(TestCase):
    """Tests for the HomeSlider model."""

    def setUp(self):
        """Set up test fixtures."""
        self.slider = HomeSlider.objects.create(
            title='Summer Beach'
        )

    def test_slider_creation(self):
        """Test that a slider is created correctly."""
        self.assertEqual(self.slider.title, 'Summer Beach')

    def test_slider_str(self):
        """Test the string representation of a slider."""
        expected_str = 'Summer Beach'
        self.assertEqual(str(self.slider), expected_str)

