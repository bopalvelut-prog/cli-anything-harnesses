import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ingress running')
@cli.command()
def start(): click.echo('ingress started')
if __name__ == '__main__': cli()
