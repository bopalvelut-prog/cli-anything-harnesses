import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ordinary running')
@cli.command()
def start(): click.echo('ordinary started')
if __name__ == '__main__': cli()
