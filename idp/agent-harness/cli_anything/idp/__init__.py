import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('idp running')
@cli.command()
def start(): click.echo('idp started')
if __name__ == '__main__': cli()
