import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gcp_redis running')
@cli.command()
def start(): click.echo('gcp_redis started')
if __name__ == '__main__': cli()
