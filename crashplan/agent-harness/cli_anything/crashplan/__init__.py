import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('CrashPlan status')
@cli.command()
def backup(): click.echo('CrashPlan backup')
if __name__ == '__main__': cli()
