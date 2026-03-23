import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grant running')
@cli.command()
def start(): click.echo('grant started')
if __name__ == '__main__': cli()
