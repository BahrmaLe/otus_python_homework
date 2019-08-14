from unittest import TestCase
from unittest.mock import patch


class APITests(TestCase):
    def test_urls(self):
        with patch('API.tests.test_urls') as mock_request:
            response = mock_request.return_value.status_code = 200

            self.assertEqual(response, 200)

    def test_all_breeds(self):
        with patch('API.tests.test_list_all_breeds') as mock_request:
            response = mock_request.return_value = {'message':
                                                        {'affenpinscher': [],
                                                         'african': [],
                                                         'airedale': [],
                                                         'akita': [],
                                                         'appenzeller': [],
                                                         'basenji': [],
                                                         'beagle': [],
                                                         'bluetick': [],
                                                         'borzoi': [],
                                                         'bouvier': [],
                                                         'boxer': [],
                                                         'brabancon': [],
                                                         'briard': [],
                                                         'bulldog': ['boston', 'english', 'french'],
                                                         'bullterrier': ['staffordshire'],
                                                         'cairn': [],
                                                         'cattledog': ['australian'],
                                                         'chihuahua': [],
                                                         'chow': [],
                                                         'clumber': [],
                                                         'cockapoo': [],
                                                         'collie': ['border'],
                                                         'coonhound': [],
                                                         'corgi': ['cardigan'],
                                                         'cotondetulear': [],
                                                         'dachshund': [],
                                                         'dalmatian': [],
                                                         'dane': ['great'],
                                                         'deerhound': ['scottish'],
                                                         'dhole': [],
                                                         'dingo': [],
                                                         'doberman': [],
                                                         'elkhound': ['norwegian'],
                                                         'entlebucher': [],
                                                         'eskimo': [],
                                                         'frise': ['bichon'],
                                                         'germanshepherd': [],
                                                         'greyhound': ['italian'],
                                                         'groenendael': [],
                                                         'hound': ['afghan', 'basset', 'blood', 'english', 'ibizan',
                                                                   'walker'],
                                                         'husky': [],
                                                         'keeshond': [],
                                                         'kelpie': [],
                                                         'komondor': [],
                                                         'kuvasz': [],
                                                         'labrador': [],
                                                         'leonberg': [],
                                                         'lhasa': [],
                                                         'malamute': [],
                                                         'malinois': [],
                                                         'maltese': [],
                                                         'mastiff': ['bull', 'english', 'tibetan'],
                                                         'mexicanhairless': [],
                                                         'mix': [],
                                                         'mountain': ['bernese', 'swiss'],
                                                         'newfoundland': [],
                                                         'otterhound': [],
                                                         'papillon': [],
                                                         'pekinese': [],
                                                         'pembroke': [],
                                                         'pinscher': ['miniature'],
                                                         'pointer': ['german', 'germanlonghair'],
                                                         'pomeranian': [],
                                                         'poodle': ['miniature', 'standard', 'toy'],
                                                         'pug': [],
                                                         'puggle': [],
                                                         'pyrenees': [],
                                                         'redbone': [],
                                                         'retriever': ['chesapeake', 'curly', 'flatcoated', 'golden'],
                                                         'ridgeback': ['rhodesian'],
                                                         'rottweiler': [],
                                                         'saluki': [],
                                                         'samoyed': [],
                                                         'schipperke': [],
                                                         'schnauzer': ['giant', 'miniature'],
                                                         'setter': ['english', 'gordon', 'irish'],
                                                         'sheepdog': ['english', 'shetland'],
                                                         'shiba': [],
                                                         'shihtzu': [],
                                                         'spaniel': ['blenheim', 'brittany', 'cocker', 'irish',
                                                                     'japanese', 'sussex', 'welsh'],
                                                         'springer': ['english'],
                                                         'stbernard': [],
                                                         'terrier': ['american', 'australian', 'bedlington', 'border',
                                                                     'dandie', 'fox', 'irish', 'kerryblue', 'lakeland',
                                                                     'norfolk', 'norwich', 'patterdale', 'russell',
                                                                     'scottish', 'sealyham', 'silky', 'tibetan', 'toy',
                                                                     'westhighland', 'wheaten', 'yorkshire'],
                                                         'vizsla': [],
                                                         'weimaraner': [],
                                                         'whippet': [],
                                                         'wolfhound': ['irish']},
                                                    'status': 'success'}

            self.assertEqual(response["status"], "success")
            self.assertTrue(response["message"])
            self.assertIsInstance(response, dict)

    def test_random(self):
        with patch('API.tests.test_random_image') as mock_request:
            response = mock_request.return_value = {'message': 'https://images.dog.ceo/breeds/dachshund/daschund-1.jpg',
                                                    'status': 'success'}
            response2 = mock_request.return_value = {'message': 'https://images.dog.ceo/breeds/terrier-yorkshire/n02094433_194.jpg',
                                                     'status': 'success'}

            self.assertNotEqual(response, response2)

    def test_random_three(self):
        with patch('API.tests.test_random_three_image') as mock_request:
            response = mock_request.return_value = {'message': ['https://images.dog.ceo/breeds/spaniel-irish/n02102973_2579.jpg',
                                                                'https://images.dog.ceo/breeds/coonhound/n02089078_4422.jpg',
                                                                'https://images.dog.ceo/breeds/keeshond/n02112350_2211.jpg'],
                                                    'status': 'success'}

            response2 = mock_request.return_value = {'message': ['https://images.dog.ceo/breeds/komondor/n02105505_3008.jpg',
                                                                 'https://images.dog.ceo/breeds/mix/squeeze-domastif-chibul-1.jpg',
                                                                 'https://images.dog.ceo/breeds/bullterrier-staffordshire/n02093256_2763.jpg'],
                                                     'status': 'success'}
            self.assertNotEqual(response, response2)

    def test_images_breed(self):
        with patch('API.tests.test_images_by_breed') as mock_request:
            response = mock_request.return_value = {'message': ['https://images.dog.ceo/breeds/hound-english/n02102973_2579.jpg',
                                                                'https://images.dog.ceo/breeds/hound-english/n02089078_4422.jpg',
                                                                'https://images.dog.ceo/breeds/hound-english/n02112350_2211.jpg'
                                                                'https://images.dog.ceo/breeds/hound-english/n02105505_3008.jpg',
                                                                'https://images.dog.ceo/breeds/hound-english/squeeze-domastif-chibul-1.jpg',
                                                                'https://images.dog.ceo/breeds/hound-english/n02093256_2763.jpg'],
                                                    'status': 'success'}
            for i in (response['message']):
                self.assertIn("hound", i)

            self.assertEqual(response['status'], 'success')
            self.assertIsInstance(response['message'], list)

    def test_random_image_breed(self):
        with patch('API.tests.test_random_image_by_breed') as mock_request:
            response = mock_request.return_value = {
                'message': 'https://images.dog.ceo/breeds/hound-english/n02089973_3820.jpg',
                'status': 'success'}
            response2 = mock_request.return_value = {
                'message': 'https://images.dog.ceo/breeds/hound-basset/n02088238_9725.jpg',
                'status': 'success'}
            self.assertNotEqual(response, response2)

    def test_random_three_image_breed(self):
        with patch('API.tests.test_random_three_image_by_breed') as mock_request:
            response = mock_request.return_value = {
                'message': ['https://images.dog.ceo/breeds/hound-afghan/n02088094_4396.jpg',
                            'https://images.dog.ceo/breeds/hound-basset/n02088238_12196.jpg',
                            'https://images.dog.ceo/breeds/hound-english/n02089973_1733.jpg'],
                'status': 'success'}
            response2 = mock_request.return_value = {
                'message': ['https://images.dog.ceo/breeds/hound-basset/n02088238_1944.jpg',
                            'https://images.dog.ceo/breeds/hound-blood/n02088466_7195.jpg',
                            'https://images.dog.ceo/breeds/hound-walker/n02089867_1430.jpg'],
                'status': 'success'}

            self.assertNotEqual(response, response2)
            self.assertEqual(len(response['message']), len(response2['message']))
            for i in (response['message']):
                self.assertIn('hound', i)
            for i in (response2['message']):
                self.assertIn('hound', i)

    def test_all_subbreeds(self):
        with patch('API.tests.test_list_all_subbreeds') as mock_request:
            response = mock_request.return_value = {'message': ['afghan',
                                                                'basset',
                                                                'blood',
                                                                'english',
                                                                'ibizan',
                                                                'walker'],
                                                    'status': 'success'}

            self.assertEqual(response['status'], 'success')
            self.assertEqual(len(response['message']), 6)
            self.assertIsInstance(response['message'], list)

    def test_images_subbreed(self):
        with patch('API.tests.test_images_by_subbreed') as mock_request:
            response = mock_request.return_value = {
                'message': ['https://images.dog.ceo/breeds/hound-afghan/n02088094_1023.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_1724.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_649.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_1917.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_3588.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_515.jpg'],
                'status': 'success'}

            self.assertEqual(response['status'], 'success')
            self.assertIsInstance(response['message'], list)
            for i in (response['message']):
                self.assertIn('afghan', i)

    def test_random_image_subbreed(self):
        with patch('API.tests.test_random_image_by_subbreed') as mock_request:
            response = mock_request.return_value = {
                'message': 'https://images.dog.ceo/breeds/hound-afghan/n02088094_1023.jpg',
                'status': 'success'}
            response2 = {
                'message': 'https://images.dog.ceo/breeds/hound-afghan/n02088094_1917.jpg',
                'status': 'success'}

            self.assertNotEqual(response, response2)
            self.assertIn('afghan', response['message'])
            self.assertIn('afghan', response2['message'])

    def test_random_three_image_subbreed(self):
        with patch('API.tests.test_random_three_image_by_subbreed') as mock_request:
            response = mock_request.return_value = {
                'message': ['https://images.dog.ceo/breeds/hound-afghan/n02088094_1023.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_1724.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_649.jpg'],
                'status': 'success'}
            response2 = {
                'message': ['https://images.dog.ceo/breeds/hound-afghan/n02088094_1917.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_3588.jpg',
                            'https://images.dog.ceo/breeds/hound-afghan/n02088094_515.jpg'],
                'status': 'success'}

            self.assertNotEqual(response, response2)
            for i in (response['message']):
                self.assertIn('afghan', i)
            for i in (response2['message']):
                self.assertIn('afghan', i)



