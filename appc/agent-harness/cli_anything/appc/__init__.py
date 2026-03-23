import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appc running')
@cli.command()
def start(): click.echo('appc started')
if __name__ == '__main__': cli()
