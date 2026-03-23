import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('loadbalancer running')
@cli.command()
def start(): click.echo('loadbalancer started')
if __name__ == '__main__': cli()
