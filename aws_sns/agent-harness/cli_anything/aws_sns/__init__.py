import click
@click.group()
def cli(): pass
@cli.command()
def topics(): click.echo('SNS topics')
@cli.command()
def publish(): click.echo('SNS publish')
if __name__ == '__main__': cli()
