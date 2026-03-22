
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('image')
@click.argument('output')
@click.option('-l', '--lang', default='eng')
def ocr(image, output, lang):
    subprocess.run(['tesseract', image, output, '-l', lang]); click.echo(f'OCR done: {output}.txt')
@cli.command()
def languages():
    click.echo('eng, fin, swe, deu, fra, spa, ita, por, rus, chi_sim, jpn, kor')
if __name__ == '__main__': cli()
