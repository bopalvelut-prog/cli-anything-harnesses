import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grpcurl running')
@cli.command()
def start(): click.echo('grpcurl started')
if __name__ == '__main__': cli()
