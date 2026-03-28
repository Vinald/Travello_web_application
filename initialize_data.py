"""
Management command to initialize the database with sample data.
Run with: python manage.py shell < initialize_data.py
"""

from destination.models import Destination, NewsPosts, Testimonial, HomeSlider
from contact.models import Contact

# Clear existing data (optional)
# Destination.objects.all().delete()
# NewsPosts.objects.all().delete()
# Testimonial.objects.all().delete()
# HomeSlider.objects.all().delete()

# Create sample destinations
destinations_data = [
    {
        'name': 'Paris, France',
        'price': 1200,
        'description': 'The City of Light awaits you with iconic landmarks like the Eiffel Tower and charming cafés.',
        'offer': True,
    },
    {
        'name': 'Tokyo, Japan',
        'price': 1800,
        'description': 'Experience the blend of ancient traditions and cutting-edge technology in this vibrant metropolis.',
        'offer': False,
    },
    {
        'name': 'Bali, Indonesia',
        'price': 800,
        'description': 'Tropical paradise with beautiful beaches, rice terraces, and rich cultural heritage.',
        'offer': True,
    },
    {
        'name': 'Barcelona, Spain',
        'price': 950,
        'description': 'Gothic quarters, stunning architecture by Gaudí, and vibrant nightlife await you.',
        'offer': False,
    },
    {
        'name': 'New York, USA',
        'price': 1500,
        'description': 'The city that never sleeps offers world-class museums, Broadway shows, and iconic landmarks.',
        'offer': False,
    },
    {
        'name': 'Dubai, UAE',
        'price': 1100,
        'description': 'Luxury shopping, modern skyscrapers, and desert adventures in the heart of the Middle East.',
        'offer': True,
    },
]

print("Creating destinations...")
for data in destinations_data:
    destination, created = Destination.objects.get_or_create(
        name=data['name'],
        defaults={
            'price': data['price'],
            'description': data['description'],
            'offer': data['offer'],
        }
    )
    if created:
        print(f"✓ Created: {destination.name}")
    else:
        print(f"→ Already exists: {destination.name}")

# Create sample news posts
news_data = [
    {
        'title': 'Top 10 Hidden Gems in Europe',
        'date': 15,
        'month': 'March',
        'category': 'Travel Tips',
        'content': 'Discover lesser-known destinations that offer authentic European experiences away from crowded tourist spots.',
    },
    {
        'title': 'Budget Travel Guide to Southeast Asia',
        'date': 20,
        'month': 'March',
        'category': 'Budget Travel',
        'content': 'Travel through Thailand, Vietnam, and Cambodia without breaking the bank. Tips for budget-conscious travelers.',
    },
    {
        'title': 'Best Time to Visit the Caribbean',
        'date': 10,
        'month': 'March',
        'category': 'Destination Guides',
        'content': 'Plan your perfect Caribbean vacation with our comprehensive guide on the best times to visit different islands.',
    },
]

print("\nCreating news posts...")
for data in news_data:
    news, created = NewsPosts.objects.get_or_create(
        title=data['title'],
        defaults={
            'date': data['date'],
            'month': data['month'],
            'category': data['category'],
            'content': data['content'],
        }
    )
    if created:
        print(f"✓ Created: {news.title}")
    else:
        print(f"→ Already exists: {news.title}")

# Create sample testimonials
testimonial_data = [
    {
        'author': 'John Smith',
        'position': 'CEO, Travel Co.',
        'content': 'Excellent service! The team made our vacation unforgettable. Highly recommended!',
    },
    {
        'author': 'Sarah Johnson',
        'position': 'Travel Blogger',
        'content': 'Professional service with great attention to detail. Perfect for wanderlust seekers!',
    },
    {
        'author': 'Michael Chen',
        'position': 'Business Traveler',
        'content': 'Outstanding support and competitive pricing. Will definitely book again!',
    },
]

print("\nCreating testimonials...")
for data in testimonial_data:
    testimonial, created = Testimonial.objects.get_or_create(
        author=data['author'],
        defaults={
            'position': data['position'],
            'content': data['content'],
        }
    )
    if created:
        print(f"✓ Created: {testimonial.author}")
    else:
        print(f"→ Already exists: {testimonial.author}")

# Create sample home sliders
slider_data = [
    {'title': 'Summer Beach Paradise'},
    {'title': 'Mountain Adventure'},
    {'title': 'City Exploration'},
]

print("\nCreating home sliders...")
for data in slider_data:
    slider, created = HomeSlider.objects.get_or_create(
        title=data['title'],
        defaults={}
    )
    if created:
        print(f"✓ Created: {slider.title}")
    else:
        print(f"→ Already exists: {slider.title}")

print("\n✓ Sample data initialization completed!")

