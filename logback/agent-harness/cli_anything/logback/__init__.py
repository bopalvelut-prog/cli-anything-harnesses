import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('logback running')
@cli.command()
def start(): click.echo('logback started')
if __name__ == '__main__': cli()
