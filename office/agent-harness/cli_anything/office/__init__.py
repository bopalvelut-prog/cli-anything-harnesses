import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('office running')
@cli.command()
def start(): click.echo('office started')
if __name__ == '__main__': cli()
