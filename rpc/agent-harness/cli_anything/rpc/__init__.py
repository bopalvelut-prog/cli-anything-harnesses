import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rpc running')
@cli.command()
def start(): click.echo('rpc started')
if __name__ == '__main__': cli()
