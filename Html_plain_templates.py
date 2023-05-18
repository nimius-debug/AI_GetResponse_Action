# *****************************************Template1*************************************************************************************
def html_tamplate(book_title, subject, img_link, summary, practical_use, book_link ):
    html_email = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{book_title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 2.2;
                width: 100%;
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }}
            h1 {{
                font-size: 24px;
                margin-top: 30px;
                margin-bottom: 20px;
            }}
            .container p {{
                font-size:16px;
                line-height: 2.2;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding-top:5px;
                padding-bottom:30px;
                padding-right:30px;
                padding-left:30px;
                background-color: #F7FCFD;
                border-style: outset;
                border-radius: 5px;
                border-width:2px;
                line-height: 1.5;
                
            }}
           
            .signature {{
                font-family: cursive;
                font-size: 1rem;
                line-height: 1;
            }}
            .bottom {{
                background-color: #333;
                color: #fff;
                padding: 20px;
                font-size: 14px;
            }}
           
        </style>
    </head>
    <body>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <td align="center">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: 0 auto;">
                        <tr>
                            <td>
                                <div class="container">
                                    {''.join([f'<p>{sentence}</p>' for sentence in summary])}
                                    
                                   
                                    <h3>Book Nugget 📖 </h3>
                                    
                                    {''.join([f'<p>{sentence}</p>' for sentence in practical_use])}
                                    
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td class="bottom">
                                <p class="signature">"Stay Nuggety"</p>
                                <p class="signature">- Jorge A. Gil </p>
                                <p> &copy; 2023 JAG LLC. All rights reserved.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    return html_email


# *****************************************Template2*************************************************************************************
def plain_text_tamplate(subject, img_link,summary, practical_use, book_link):
    plain_text_email = f"""{subject} {img_link} {summary} Real One: {practical_use} More Real Ones >>>>>{book_link} Read me!"""
    
    return plain_text_email


def simple_html_tamplate(book_title,subject, img_link, summary, practical_use ):
    html_email = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{subject}</title>
    </head>
    <body style="font-family: Arial, Helvetica, sans-serif; background-color: #f2f2f2;">
        <div style="max-width: 600px; margin: 0 auto;padding: 10px">
            <div style="padding: 20px; line-height:2.2; font-size: 16px; background-color: #ffffff;">
            <img style="float: left; margin-right: 20px;" src={img_link} alt={book_title}>
            {''.join([f'<p>{sentence}</p>' for sentence in summary])}

            <h3>Book Nugget 📖 </h3>
                                            
            {''.join([f'<p>{sentence}</p>' for sentence in practical_use])}
            
            </div>
            <div style="font-size: 14px; margin-left: 20px; font-weight: bold;">
            <p>"Stay Nuggety"</p>
            <p>Jorge A. Gil </p>
            <p> &copy; 2023 JAG LLC. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>

    """
    return html_email

def simple_plain_text_tamplate(book_title,subject, img_link,summary, practical_use):
    plain_text_email = f"""{subject} {img_link} {book_title} {summary} Book Nugget 📖 {practical_use} Stay Nuggety Jorge A. Gil &copy; 2023 JAG LLC. All rights reserved."""
    return plain_text_email
