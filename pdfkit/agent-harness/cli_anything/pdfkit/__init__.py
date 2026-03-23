import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pdfkit running')
@cli.command()
def start(): click.echo('pdfkit started')
if __name__ == '__main__': cli()
