import click
@click.group()
def cli(): pass
@cli.command()
def topics(): click.echo('Pub/Sub topics')
@cli.command()
def publish(): click.echo('Pub/Sub publish')
if __name__ == '__main__': cli()
