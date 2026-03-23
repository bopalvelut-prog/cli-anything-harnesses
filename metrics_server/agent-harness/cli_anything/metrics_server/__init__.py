import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('metrics_server running')
@cli.command()
def start(): click.echo('metrics_server started')
if __name__ == '__main__': cli()
