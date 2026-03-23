import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_inspector running')
@cli.command()
def start(): click.echo('amazon_inspector started')
if __name__ == '__main__': cli()
