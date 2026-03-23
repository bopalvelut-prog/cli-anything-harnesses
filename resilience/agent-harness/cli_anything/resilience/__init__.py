import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resilience running')
@cli.command()
def start(): click.echo('resilience started')
if __name__ == '__main__': cli()
