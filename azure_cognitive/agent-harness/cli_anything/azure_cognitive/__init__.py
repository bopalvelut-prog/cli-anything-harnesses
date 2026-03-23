import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_cognitive running')
@cli.command()
def start(): click.echo('azure_cognitive started')
if __name__ == '__main__': cli()
