import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('joi running')
@cli.command()
def start(): click.echo('joi started')
if __name__ == '__main__': cli()
