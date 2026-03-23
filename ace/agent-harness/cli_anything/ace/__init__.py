import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ace running')
@cli.command()
def start(): click.echo('ace started')
if __name__ == '__main__': cli()
