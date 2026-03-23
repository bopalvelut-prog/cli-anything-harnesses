import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_videoanalyzer running')
@cli.command()
def start(): click.echo('azure_videoanalyzer started')
if __name__ == '__main__': cli()
