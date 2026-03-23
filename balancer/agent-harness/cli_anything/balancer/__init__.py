import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('balancer running')
@cli.command()
def start(): click.echo('balancer started')
if __name__ == '__main__': cli()
