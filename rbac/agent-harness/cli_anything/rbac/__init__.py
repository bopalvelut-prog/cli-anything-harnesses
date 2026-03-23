import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rbac running')
@cli.command()
def start(): click.echo('rbac started')
if __name__ == '__main__': cli()
