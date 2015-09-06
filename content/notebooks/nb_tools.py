import os
from datetime import datetime

def connect_notebook_to_post(name='Untitled', title='New post', tags='ipython'):
    """
    Write a header to a markdown blog post and return an HTML string with links to the notebook.
    
    Idea taken from http://ocefpaf.github.com/python4oceanographers
    """

    hour = datetime.utcnow().strftime('%H:%M')

    date = '-'.join(name.split('-')[:3])

    metadata = dict(title=title,
                    date=date,
                    hour=hour,
                    tags=tags,
                    name=name)

    markdown = "Title: {title}\ndate: {date} {hour}\ntags: {tags}\n\n{{% notebook {name}.ipynb cells[2:] %}}".format(**metadata)

    content = os.path.abspath(os.path.join(os.getcwd(),
                                           os.pardir,
                                           '{}.md'.format(name)))
    with open('{}'.format(content), 'w') as f:
        f.writelines(markdown)

    html = """
    <small>
    <p> This post was written as an IPython notebook. You can view it as a static 
    <a href="http://nbviewer.ipython.org/github/dennissergeev/dennissergeev.github.io/blob/src/content/notebooks/%s.ipynb">HTML file</a> or 
    <a href="https://raw.githubusercontent.com/dennissergeev/dennissergeev.github.io/src/content/notebooks/%s.ipynb">download the source</a>.</p>
    """ % (name, name)

    return html
