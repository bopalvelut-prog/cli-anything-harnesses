import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_kinesis running')
@cli.command()
def start(): click.echo('aws_kinesis started')
if __name__ == '__main__': cli()
