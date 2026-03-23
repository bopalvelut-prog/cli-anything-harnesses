import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('manage running')
@cli.command()
def start(): click.echo('manage started')
if __name__ == '__main__': cli()
