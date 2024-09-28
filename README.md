# Recipe Recommender System"



This is a **Recipe Recommender System** that suggests food recepies based on user preferences. The system uses machine learning techniques to recommend food items tailored to users' taste profiles and dietary habits.
_
<img width="1440" alt="Screenshot 2024-09-28 at 9 17 39 AM" src="https://github.com/user-attachments/assets/3b84845b-7afa-4e4d-8fcb-2f58f4af5e1c">
<img width="1440" alt="Screenshot 2024-09-28 at 9 18 04 AM" src="https://github.com/user-attachments/assets/8aaa0c36-00d3-4f7c-9db8-1dff168a6946">


## Used Dataset - https://www.kaggle.com/datasets/elisaxxygao/foodrecsysv1

## Features
- Content-Based Recommendations (Used ingredients and nutirions as base for content-based filtering. Used Word2vec technique to convert ingredients into vector form.)
- Popularity Based Recommendations (Filtered the top 50 recipes from the dataset to show them upfront when user open the application.)
- Machine learning-based recommendation algorithms.
![Screenshot from 2024-05-25 13-31-09](https://github.com/SuyashDahale13/Food_Recommender_System/assets/138577127/7a52b266-4a86-40b4-8cb6-dfc6d7c72822)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone -b Version_1.1 https://github.com/SuyashDahale13/Food_Recommender_System.git
   cd Food_Recommender_System/Food
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   # OR
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies:**
   Install the required Python packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
4. **Copy Images :**
   Download the [dataset](https://www.kaggle.com/datasets/elisaxxygao/foodrecsysv1) and move "raw-data-images" folder into static folder (inside recommender_system folder)

5. **Setup the database (if applicable):**
   I have used postgresql with [pgvector](https://github.com/pgvector/pgvector) extension to store vectors.
   check my [food.ipynb](https://github.com/SuyashDahale13/Recipe_Recommender_System/blob/Version_1.1/food.ipynb)
   ```bash
   python manage.py migrate
   ```
5. **Collect static files:**
   ```bash
   pthon manage.py collectstatic
   ```
6. **Run the development server:**
   Start the Django development server to run the application locally:
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Food Recommender System.

## Usage
1. User can pick recipe from top recipes.
2. User can check the nutritions values and recipe instructions on "Details" page.
3. User can search recipe from searchbar.
4. User can check all the available recipes in available in database.

## Technologies Used
- **Backend**: Django (Python framework)
- **Frontend**: HTML, CSS
- **Database**: Postgresql + pgvector
- **Machine Learning**: Scikit-learn, vector database, word2vec

## Contributing
We welcome contributions to improve the Food Recommender System! To contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please reach out at [your-email@example.com](mailto:suyashdahaleatwork@gmail.com).

---

