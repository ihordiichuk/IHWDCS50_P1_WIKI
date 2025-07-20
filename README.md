# CS50 Web Development - Project 1: Wiki

A Django-based Wikipedia-like encyclopedia application built as part of Harvard's CS50 Web Development course.

## Features Implemented

✅ **Entry Pages** - View encyclopedia entries with Markdown to HTML conversion  
✅ **Index Page** - Browse all available entries with clickable links  
✅ **Search Functionality** - Search with exact match redirect and substring results  
✅ **Create New Pages** - Add new encyclopedia entries with duplicate prevention  
✅ **Edit Existing Pages** - Modify entry content with pre-populated forms  
✅ **Random Page** - Navigate to a random encyclopedia entry  
✅ **Error Handling** - User-friendly error pages and input validation  

## Technologies Used

- **Django** - Web framework
- **Python** - Backend programming
- **Markdown2** - Markdown to HTML conversion
- **Bootstrap** - Frontend styling
- **HTML/CSS** - Frontend markup and styling

## Project Structure

```
wiki/
├── encyclopedia/          # Main Django app
│   ├── templates/        # HTML templates
│   ├── static/          # CSS and static files
│   ├── views.py         # Application views
│   └── urls.py          # URL routing
├── entries/             # Markdown encyclopedia entries
├── wiki/                # Django project settings
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ihordiichuk/IHWDCS50_P1_WIKI.git
   cd IHWDCS50_P1_WIKI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to `http://127.0.0.1:8000`

## Requirements Fulfilled

This project fulfills all CS50 Web Development Project 1 requirements:

- ✅ Entry Page functionality
- ✅ Index Page with clickable links
- ✅ Search with exact and substring matching
- ✅ New Page creation with validation
- ✅ Edit Page functionality
- ✅ Random Page navigation
- ✅ Markdown to HTML conversion

## Course Information

**Course:** [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)  
**Project:** Project 1 - Wiki  
**Institution:** Harvard University  

## Author

**Ihor Hordiichuk**  
CS50 Web Development Student
