import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bleed running')
@cli.command()
def start(): click.echo('bleed started')
if __name__ == '__main__': cli()
