import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vcpu running')
@cli.command()
def start(): click.echo('vcpu started')
if __name__ == '__main__': cli()
