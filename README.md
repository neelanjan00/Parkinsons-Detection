<h1 align="center">Welcome to Parkinsons AI 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/NeelanjanManna" target="_blank">
    <img alt="Twitter: NeelanjanManna" src="https://img.shields.io/twitter/follow/NeelanjanManna.svg?style=social" />
  </a>
</p>

>[This is the backend API of the project, the frontend mobile app can be found <a href="https://google.com">here</a>] Project descriptionAn AI based mobile application which is able to diagnose the Parkinson's Disease using two independent tests that require only a pencil and a paper. Based on 2017 research paper Distinguishing Different Stages of Parkinson's Disease Using Composite Index of Speed and Pen-Pressure of Sketching a Spiral by Zham et. al. The trained models were deployed using a Flask backend server, along with a Flutter based frontend mobile application frontend to interact with the REST API.

### 🏠 [Homepage](https://github.com/neelanjan00/Parkinson-s-Detection)

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python app.py
```
## API Routes
| Route  | Method | Field Name | Input Type | Returns |
|:-------|--------|------------|------------|:------------|
| `/spiral` | POST | InputImg | Image File (png or jpg or jpeg) | Returns the string "Healthy" or "Parkinson's Disease". |
| `/wave` | POST | InputImg | Image File (png or jpg or jpeg) | Returns the string "Healthy" or "Parkinson's Disease". |

## Author

👤 **Neelanjan Manna**

* Website: https://neelanjanmanna.ml/
* Twitter: [@NeelanjanManna](https://twitter.com/NeelanjanManna)
* Github: [@neelanjan00](https://github.com/neelanjan00)
* LinkedIn: [@neelanjan00](https://linkedin.com/in/neelanjan00)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_