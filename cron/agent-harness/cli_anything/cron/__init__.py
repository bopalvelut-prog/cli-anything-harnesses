import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): subprocess.run(['crontab', '-l'])
@cli.command()
def edit(): subprocess.run(['crontab', '-e'])
@cli.command()
@click.argument('schedule')
@click.argument('cmd')
def add(schedule, cmd): click.echo(f'Add: {schedule} {cmd}')
if __name__ == '__main__': cli()
