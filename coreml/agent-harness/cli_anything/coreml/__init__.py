import click
@click.group()
def cli(): pass
@cli.command()
def convert(): click.echo('CoreML convert')
@cli.command()
def predict(): click.echo('CoreML predict')
if __name__ == '__main__': cli()
