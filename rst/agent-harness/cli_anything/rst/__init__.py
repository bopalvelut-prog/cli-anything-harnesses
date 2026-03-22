import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
def html(input): subprocess.run(['rst2html', input])
@cli.command()
@click.argument('input')
def pdf(input): subprocess.run(['rst2pdf', input])
if __name__ == '__main__': cli()
