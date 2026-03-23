import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_eventgrid_v2 running')
@cli.command()
def start(): click.echo('azure_eventgrid_v2 started')
if __name__ == '__main__': cli()
