import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ganglia running')
@cli.command()
def start(): click.echo('ganglia started')
if __name__ == '__main__': cli()
