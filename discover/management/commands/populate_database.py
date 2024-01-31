from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from discover.models import DiscoverThread, Source
import random

class Command(BaseCommand):
    help = 'Populate database with mock data'

    def handle(self, *args, **options):

        # Create mock Sources
        source_urls = [
            "https://www.theverge.com/2024/1/30/24055718/new-york-times-generative-ai-machine-learning",
            "https://www.nytimes.com/2023/07/19/business/google-artificial-intelligence-news-articles.html",
            "https://www.wsj.com/business/media/new-york-times-hires-first-newsroom-leader-focused-on-artificial-intelligence-facc83f1",
            "https://neuralink.com/blog/first-clinical-trial-open-for-recruitment/",
            "https://finance.yahoo.com/news/neuralink-implants-brain-chip-first-231000125.html",
            "https://nordvpn.com/cybersecurity/glossary/data-poisoning/",
            "https://paperswithcode.com/task/data-poisoning",
        ]
        sources = [Source.objects.create(url=url) for url in source_urls]

        # Create mock DiscoverThreads
        discover_threads_data = [
            {
                'title': 'What is data poisoning?',
                'description': 'Data poisoning is a type of cyber attack that targets machine learning models by tampering with their training data. The goal of these attacks is to manipulate the models behavior by introducing, modifying, or deleting data points in the training dataset. This can lead to the model making incorrect decisions or predictions once deployed. The success of a data poisoning attack depends on the stealthiness of the poisoned data to avoid detection during data cleaning or preprocessing, and the efficacy of the attack in degrading model performance. Data poisoning can have serious implications, especially as more businesses rely on AI and machine learning systems. It can be used for various malicious purposes, including disinformation, phishing scams, altering public opinion, or discrediting individuals or brands',
                'views': 100,
                'branches': 10,
                'datetime': timezone.now(),
                'image_url': "https://www.seahouseimagery.com/cdn/shop/products/WM_Blue_Water_1080x.jpg?v=1560578927".format(),
            },
            {
                'title': 'The moon is shrinking',
                'description': """Yes, the moon is indeed shrinking, albeit very slowly. This shrinkage is due to the cooling of the moon's interior, which has caused it to contract by more than 150 feet in circumference over the last several hundred million years.

                            The shrinking process is similar to how a grape wrinkles when it becomes a raisin. However, unlike a grape's flexible skin, the moon's surface is brittle. This brittleness leads to the formation of "thrust faults" where sections of the crust push up against each other.

                            The formation of these faults is often accompanied by seismic activity, known as moonquakes, which are similar to earthquakes on Earth. These moonquakes can last for hours and even an entire afternoon, posing potential risks to future human missions, particularly in areas near or within these fault zones.

                            A recent study has linked a group of faults in the moon's south polar region to a powerful moonquake recorded in the past. This region is of particular interest as it is where NASA hopes to land during the crewed Artemis III mission. The study also found that some areas in this region are unstable due to the moon's ongoing shrinkage, which could lead to landslides and other surface instabilities.

                            This new understanding of the moon's shrinkage and the associated seismic risks is crucial for the safe planning of future moon missions.
                            """,
                'views': 312,
                'branches': 92,
                'datetime': timezone.now() - timezone.timedelta(days=2),
                'image_url': "https://cdn1.vectorstock.com/i/1000x1000/58/15/square-shaped-fried-egg-vector-20135815.jpg",
            },
            {
                'title': 'Reddit $5 billion valuation',
                'description': """Reddit is reportedly considering a valuation of at least $5 billion for its upcoming Initial Public Offering (IPO). This valuation is based on feedback from early meetings with potential investors. However, private trades of Reddit's unlisted shares have indicated a lower valuation, between $4.5 billion and $4.8 billion.

                        The final valuation will depend on the recovery of the IPO market. Reddit's advisers are targeting a valuation in the mid-single-digit billions, but the exact timing and valuation could change. The company is considering a possible listing as soon as March.

                        It's worth noting that Reddit had raised funds at a $10 billion valuation during its most recent funding round, and there were speculations that it could have been valued as much as $15 billion in an IPO. However, the current market conditions and the performance of tech IPOs in recent years seem to have influenced the lower target valuation.

                        Reddit's decision to go public is significant, as it would be the first major social media platform to do so since Pinterest's IPO in 2019. The company has more than 70 million daily active unique visitors and more than 100,000 active communities, according to stats on its website.
                        """,
                'views': 150,
                'branches': 13,
                'datetime': timezone.now() - timezone.timedelta(hours=3),
                'image_url': "https://pplx-res.cloudinary.com/image/fetch/s--7rBGk--z--/t_thumbnail/https://www.creativeboom.com/upload/articles/cd/cd1b08cd59d26ad43924fa2df8ed000840ce2136_1280.jpg",
            },
        ]

        for data in discover_threads_data:
            thread = DiscoverThread.objects.create(**data)
            thread.sources.set(random.sample(sources, k=3))


        self.stdout.write(self.style.SUCCESS('Successfully populated DiscoverThread instances with mock data'))
