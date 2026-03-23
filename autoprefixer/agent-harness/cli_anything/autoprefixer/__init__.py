import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autoprefixer running')
@cli.command()
def start(): click.echo('autoprefixer started')
if __name__ == '__main__': cli()
