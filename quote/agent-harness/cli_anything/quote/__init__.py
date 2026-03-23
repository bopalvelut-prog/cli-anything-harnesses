import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quote running')
@cli.command()
def start(): click.echo('quote started')
if __name__ == '__main__': cli()
