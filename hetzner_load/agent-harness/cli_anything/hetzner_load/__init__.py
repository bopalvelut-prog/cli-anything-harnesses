import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Load balancers')
@cli.command()
def create(): click.echo('Create load balancer')
if __name__ == '__main__': cli()
