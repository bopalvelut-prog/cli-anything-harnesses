import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Prisma Cloud scan')
@cli.command()
def report(): click.echo('Prisma Cloud report')
if __name__ == '__main__': cli()
