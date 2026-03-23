import click
@click.group()
def cli(): pass
@cli.command()
def tables(): click.echo('DynamoDB tables')
@cli.command()
def scan(): click.echo('DynamoDB scan')
if __name__ == '__main__': cli()
