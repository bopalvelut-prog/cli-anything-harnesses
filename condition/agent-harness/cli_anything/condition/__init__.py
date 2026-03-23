import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('condition running')
@cli.command()
def start(): click.echo('condition started')
if __name__ == '__main__': cli()
