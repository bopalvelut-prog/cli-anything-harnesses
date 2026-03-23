import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_cloudtrail running')
@cli.command()
def start(): click.echo('aws_cloudtrail started')
if __name__ == '__main__': cli()
